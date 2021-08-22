using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Lab9.Models;
using System.Web.Configuration;

namespace Laboratory_9.DataAbstractionLayer
{
    public class DAL
    {
        public MySqlConnection GetConnection()
        {
            string connectionString = "server=localhost;uid=root;pwd=;database=web;";
            return new MySqlConnection(connectionString);
        }

        public (bool, int) login(string username, string password)
        {
            List<int> users = new List<int>();
            try
            {
                MySqlConnection connection = GetConnection();
                connection.Open();

                MySqlCommand command = new MySqlCommand();
                command.Connection = connection;
                command.CommandText = "SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"'";
                MySqlDataReader reader = command.ExecuteReader();
                
                while (reader.Read())
                {
                    users.Add(reader.GetInt32("id"));
                }
                reader.Close();

                connection.Close();

                return (users.Count == 1, users[0]);

            }
            catch (MySqlException exception)
            {
                Console.Write(exception.Message);
                return (false,-1);
            }

            return (false, -1);
           
        }

        internal List<Channel> getOwnedChannels(int owner)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            List<Channel> chList = new List<Channel>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "SELECT * FROM channels where ownerid = " + owner;
                MySqlDataReader dataReader = cmd.ExecuteReader();

                while (dataReader.Read())
                {
                    Channel channel = new Channel();
                    channel.id = dataReader.GetInt32("id");
                    channel.ownerid = dataReader.GetInt32("ownerid");
                    channel.name = dataReader.GetString("name");
                    channel.subscribers = dataReader.GetString("subscribers");

                    chList.Add(channel);
                }

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return chList;
        }

        internal List<Website> getWebsites()
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            List<Website> websiteList = new List<Website>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "SELECT * FROM websites";
                MySqlDataReader dataReader = cmd.ExecuteReader();

                while (dataReader.Read())
                {
                    Website website = new Website();
                    website.id = dataReader.GetInt32("id");
                    website.url = dataReader.GetString("url");
                    websiteList.Add(website);
                }

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return websiteList;
        }

        internal List<Channel> getSubscriptions(string user)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            List<Channel> chList = new List<Channel>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "SELECT * FROM channels";
                MySqlDataReader dataReader = cmd.ExecuteReader();

                while (dataReader.Read())
                {
                    Channel channel = new Channel();
                    channel.id = dataReader.GetInt32("id");
                    channel.ownerid = dataReader.GetInt32("ownerid");
                    channel.name = dataReader.GetString("name");
                    channel.subscribers = dataReader.GetString("subscribers");

                    if(channel.subscribers.Contains(user)){
                        chList.Add(channel);
                    }
                }

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return chList;
        }

        internal int updateDoc(string name, string k1, string k2, string k3, string k4, string k5)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "UPDATE documents SET keyword1 = '" + k1 + "', keyword2 = '" + k2 + "', keyword3 = '" + k3 + "', keyword4 = '" + k4 + "', keyword5 = '" + k5 + "' where name = '" + name + "'";
                cmd.ExecuteNonQuery();
                connection.Close();

                return 1;
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
                return 0;
            }
        }

        internal void addSubscription(string user, string channel)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();


                MySqlCommand c = new MySqlCommand();
                c.Connection = connection;
                c.CommandText = "SELECT * FROM channels where name = '" + channel + "'";
                MySqlDataReader dataReader1 = c.ExecuteReader();
                dataReader1.Read();
                string subscribers = dataReader1.GetString("subscribers");

                connection.Close();
                connection.Open();

                subscribers = subscribers + user + ',';

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "update channels set subscribers = '" + subscribers + "' where name = '" + channel + "'";
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

        internal void updateSubscription(string user, string channel)
        {
            return;
        }

        internal int getOwnerByName(string owner)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand c = new MySqlCommand();
                c.Connection = connection;
                c.CommandText = "SELECT * FROM persons where name = '" + owner + "'";
                MySqlDataReader dataReader1 = c.ExecuteReader();
                dataReader1.Read();
                int ownerid = dataReader1.GetInt32("id");

                return ownerid;

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
                return - 1;
            }
        }

        internal int getDocNr(int id)
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();


                string commandText = "SELECT COUNT( idwebsite) from documents where idwebsite = " + id;


                MySqlCommand cmd = new MySqlCommand(commandText, connection);

                Int32 count = Convert.ToInt32(cmd.ExecuteScalar());


                return count;

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
                return -1;
            }
        }



        public List<Asset> getAssets()
        {
            MySqlConnection connection;
            string connectionString;

            connectionString = "server=localhost;uid=root;pwd=;database=web";
            List<Asset>  assetList = new List<Asset>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = connectionString;
                connection.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = connection;
                cmd.CommandText = "SELECT * FROM assets";
                MySqlDataReader dataReader = cmd.ExecuteReader();

                while (dataReader.Read())
                {
                    Asset asset = new Asset();
                    asset.id = dataReader.GetInt32("id");
                    asset.userid = dataReader.GetInt32("userid");
                    asset.description = dataReader.GetString("description");
                    asset.value = dataReader.GetInt32("value");

                    assetList.Add(asset);
                }

            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return assetList;
        }

    }
}