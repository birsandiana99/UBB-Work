using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ModelPractic
{
    public partial class Form1 : Form
    {
        SqlConnection connection;
        SqlDataAdapter daChild, daParent;
        DataSet ds;
        SqlCommandBuilder cb;
        BindingSource bsChild, bsParent;

        private void loadRecords()
        {
            //connection
            connection = new SqlConnection(@"Data Source = DESKTOP-S3BSAIP\SQLEXPRESS; Initial Catalog = Practic; Integrated Security = True");
            ds = new DataSet();
            daChild = new SqlDataAdapter("select * from CoffeeProducts", connection);
            daParent = new SqlDataAdapter("select * from ProductCategories", connection);
            cb = new SqlCommandBuilder(daChild);

            daParent.Fill(ds, "ProductCategories");
            daChild.Fill(ds, "CoffeeProducts");

            DataRelation dr = new DataRelation("FK_Categories_Products", ds.Tables["ProductCategories"].Columns["PCid"],
            ds.Tables["CoffeeProducts"].Columns["PCid"]);
            ds.Relations.Add(dr);

            bsParent = new BindingSource();
            bsChild = new BindingSource();

            bsParent.DataSource = ds;
            bsParent.DataMember = "ProductCategories";

            bsChild.DataSource = bsParent;
            bsChild.DataMember = "FK_Categories_Products";

            dataGridViewChild.DataSource = bsChild;
            dataGridViewParent.DataSource = bsParent;
            //loadCombo();
        }

        //insert
        private void button2_Click(object sender, EventArgs e)
        {
            try{
                daChild.InsertCommand = new SqlCommand("INSERT INTO CoffeeProducts(CPName) VALUES(@n)", connection);
                daChild.InsertCommand.Parameters.Add("@n", SqlDbType.Int).Value = Int32.Parse(tbname.Text);

                connection.Open();
                daChild.InsertCommand.ExecuteNonQuery();
                connection.Close();

                MessageBox.Show("Added succesfully!!");
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
                connection.Close();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            loadRecords();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
                MessageBox.Show("Please select a post!!");
            else
            {
                try
                {
                    var selectedRowP = Int32.Parse(dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString());
                    daChild.UpdateCommand = new SqlCommand("UPDATE CoffeeProducts SET CPName WHERE CPid = @cpid", connection);



                    daChild.UpdateCommand.Parameters.Add("@d", SqlDbType.Date).Value = DateTime.Parse(tbname.Text);
                    daChild.UpdateCommand.Parameters.Add("@pid", SqlDbType.Int).Value = selectedRowP;

                    connection.Open();
                    daChild.UpdateCommand.ExecuteNonQuery();
                    connection.Close();


                    MessageBox.Show("Updated succesfully!");

                    loadRecords();
                    loadCombo();
                }
                catch(Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
            
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
                MessageBox.Show("Please select a post!!");
            else
            {
                try
                {
                    var selectedRowP = Int32.Parse(dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString());
                    daChild.DeleteCommand = new SqlCommand("DELETE FROM CoffeeProducts WHERE CPid=@cpid", connection);
                    daChild.DeleteCommand.Parameters.Add("@cpid", SqlDbType.Int).Value = selectedRowP;

                    connection.Open();
                    daChild.DeleteCommand.ExecuteNonQuery();
                    connection.Close();

                    MessageBox.Show("Deleted succesfully!");
                    loadRecords();
                    loadCombo();

                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }

        }

        public Form1()
        {
            InitializeComponent();
        }
        private void loadCombo()
        {
         
        }
    }
}
