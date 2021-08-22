using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Laboratory_9.DataAbstractionLayer;
using Lab9.Models;
using MySqlX.XDevAPI.Relational;

namespace Lab9.Controllers
{
    public class MainController : Controller
    {
        public ActionResult Index()
        {
            return View("Main");
        }


        public ActionResult Channels()
        {
            return View("Channels");
        }

        public ActionResult Start()
        {
            return View("Start");
        }

        public ActionResult ViewAssets()
        {
            return View("ViewAssets");
        }


        public ActionResult Docs()
        {
            return View("Docs");
        }

        public String getAssets()
        {
            DAL dal = new DAL();
            List <Asset> assets = dal.getAssets();
            String output = "<table>";
            foreach(Asset a in assets){
                if(a.value > 10)
                {
                    output += "<tr class='red-row' style='background:red' "+
               "<td>" + a.id + " </td><td> " + a.userid + " </th><td>" + a.description + " </td><td>" + a.value + "</td></tr >";
                }
                else { 
	            output+= "<tr>"+
                "<td>"+ a.id + " </td><td> " + a.userid + " </th><td>"+ a.description + " </td><td>" + a.value + "</td></tr >";
                }
            }
            output+= "</table><br>";

            return output;
        }


        public String showWebsites()
        {
            DAL dal = new DAL();
            List<Website> websites = dal.getWebsites();
            String output = "<table id='mytable'> <td> ID </td><td> URL </td><td> Document </td><td> count </td></ tr >";
            foreach (Website a in websites)
            {
                output += 
                    "<tr>" +
               "<td>" + a.id + " </td><td> " + a.url + " </th><td>" + dal.getDocNr(a.id) + " </td></tr >";

                //output += "<tr>" +
                //"<td>" + a.id + " </td><td> " + a.url + "<td>" + "</td>< td > " + dal.getDocNr(a.id) + " </ td ></tr >";
                
            }
            output += "</table><br>";

            return output;
        }

        public String getOwnedChannels(int owner)
        {
            DAL dal = new DAL();
            List<Channel> channels = dal.getOwnedChannels(owner);
            String output = "<table>";
            foreach (Channel a in channels)
            {
                    output += "<tr>" +
                    "<td>" + a.name + "</td></tr >";
                
            }
            output += "</table><br>";

            return output;
        }

        public int getOwnerbyName(string owner)
        {
            DAL dal = new DAL();
            int ow = dal.getOwnerByName(owner);
            return ow;
        }


        
        public String getSubscriptions(string user)
        {
            DAL dal = new DAL();
            List<Channel> channels = dal.getSubscriptions(user);
            String output = "<table>";
            foreach (Channel a in channels)
            {
                output += "<tr>" +
                "<td>" + a.name + "</td></tr >";

            }
            output += "</table><br>";

            return output;
        }

        public int subscribe(string user, string channel)
        {
            int update = 0;
            DAL dal = new DAL();
            List<Channel> channels = dal.getSubscriptions(user);
            foreach ( Channel c in channels)
            {
                if (c.name == channel)
                {
                    update = 1;
                }
            }
            if (update == 1)
            {
                dal.updateSubscription(user, channel);
            }
            else
            {
                dal.addSubscription(user, channel);
            }
            return update;
        }


        public int updateDoc(string name, string k1, string k2, string k3, string k4, string k5)
        {
            DAL dal = new DAL();
            int update = dal.updateDoc(name, k1, k2, k3, k4, k5);
            return update;
            
        }

        

    }
}