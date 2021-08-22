using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using ASPX_mvc_example.Models;
using ASPX_mvc_example.DataAbstractionLayer;

namespace HotelRooms.Controllers
{
    public class MainController : Controller
    {
        // GET: Main
        public ActionResult Index()
        {
            return View();
        }

        public string Test()
        {
            return "It's working";
        }

        public string GetStudentsFromGroup()
        {
            int group_id = int.Parse(Request.Params["group_id"]);
            DAL dal = new DAL();
            List<Student> slist = dal.GetStudentsFromGroup(group_id);
            ViewData["studentList"] = slist;

            string result = "<table><thead><th>Id</th><th>Nume</th><th>Password</th><th>Group_Id</th></thead>";

            foreach (Student stud in slist)
            {
                result += "<tr><td>" + stud.Id + "</td><td>" + stud.Nume + "</td><td>" + stud.Password + "</td><td>" + stud.Group_id + "</td><td></tr>";
            }

            result += "</table>";
            return result;
        }
    }
}