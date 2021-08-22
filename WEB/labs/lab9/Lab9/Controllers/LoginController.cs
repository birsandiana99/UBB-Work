using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Laboratory_9.DataAbstractionLayer;

namespace Laboratory_9.Controllers
{
    public class LoginController : Controller
    {
        public ActionResult Index()
        {
            return View("Login");
        }

        public ActionResult Login()
        {
            string username = Request.Params["username"];
            string password = Request.Params["password"];

            DAL dal = new DAL();
            bool result = dal.login(username, password).Item1;
            int id = dal.login(username, password).Item2;
            return Json(new { success = result , id = id});
        }
    }
}