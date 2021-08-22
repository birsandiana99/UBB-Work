<?php


class DBUtils {
	private $host = '127.0.0.1';
	private $db = 'recipes';
	private $user = 'root';
	private $password = '';
	private $charset = 'utf8mb4';

	private $pdo;
	private $error;

	public function __construct() {
		$dsn = "mysql:host=$this->host;dbname=$this->db;charset=$this->charset";
		$opt = array(PDO::ATTR_ERRMODE			=> PDO::ERRMODE_EXCEPTION,
			PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
			PDO::ATTR_EMULATE_PREPARES	 => false);
		try {
			$this->pdo = new PDO($dsn, $this->user, $this->password, $opt);		
		}
		catch(PDOException $e){
			$this->error = $e->getMessage();
			echo "Error connecting to DB: " . $this->error;
		}
	}

	public function selectAuthor($name) {
		$stmt = $this->pdo->query("SELECT * FROM Author where Author_Name = '" . $name ."'");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}

	public function selectRecipe($name) {
		$stmt = $this->pdo->query("SELECT * FROM Recipe where Recipe_Name = '" . $name ."'");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}

	public function selectRecipeForAuthor($id) {
		$stmt = $this->pdo->query("SELECT * FROM Recipe where Recipe_Author_ID = " . $id);
		return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}

	public function selectAllRecipes() {
		$stmt = $this->pdo->query("SELECT * FROM Recipe");
		return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}

	public function selectAllAuthors() {
		$stmt = $this->pdo->query("SELECT * FROM Author");
		return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}

	public function insertAuthor($id, $name) {
		$affectedRows = $this->pdo->exec("INSERT INTO Author VALUES (" . $id . ", '" . $name . "');");
		return $affectedRows;
	}

	public function insertRecipe($raid, $ring, $rins, $rname) {
		$affectedRows = $this->pdo->exec("INSERT INTO Recipe (Recipe_Author_ID,Recipe_Ingredients,Recipe_Instructions,Recipe_Name) VALUES (" . $raid . ", '" . $ring . "', '" . $rins . "', '" . $rname . "');");
		return $affectedRows;
	}

	public function deleteAuthor($id) {
		$affectedRows = $this->pdo->exec("DELETE FROM Author WHERE Author_ID = " . $id);
		return $affectedRows;
	}

	public function deleteRecipe($id) {
		$affectedRows = $this->pdo->exec("DELETE FROM Recipe WHERE Recipe_ID = " . $id);
		return $affectedRows;
	}

	public function updateAuthor($id, $new_name) {
		$affectedRows = $this->pdo->exec("UPDATE Author SET Author_Name = '" . $new_name . "' WHERE Author_ID = " . $id);
		return $affectedRows;
	}

	public function updateRecipe($id, $new_raid, $new_ring, $new_rins, $new_rname) {
		$affectedRows = $this->pdo->exec("UPDATE Recipe SET Recipe_Author_ID = " . $new_raid . ", Recipe_Ingredients = '" . $new_ring . "', Recipe_Instructions = '" . $new_rins . "', Recipe_Name = '" . $new_rname . "' WHERE Recipe_ID = " . $id);
		return $affectedRows;
	}

	public function filterRecipes($filter) {
		$stmt = $this->pdo->query("SELECT * FROM Recipe Where Recipe_Name like '" . $filter . "%';");
		return $stmt->fetchAll(PDO::FETCH_ASSOC);
	}
}


?>