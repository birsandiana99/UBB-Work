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


        public ActionResult ViewAssets()
        {
            return View("ViewAssets");
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


    }
}