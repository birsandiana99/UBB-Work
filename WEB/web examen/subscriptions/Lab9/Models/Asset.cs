﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Lab9.Models
{
    public class Asset
    {
        public int id { get; set; }
        public int userid { get; set; }
        public string description { get; set; }
        public int value { get; set; }
    }
}