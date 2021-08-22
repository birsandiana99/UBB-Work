using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Lab9.Models;

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