<?php


require_once '../repo/DBUtils.php';
require_once 'author.php';
require_once 'recipe.php';

class Model {
	private $db;

	public function __construct() {
		$this->db = new DBUtils();
	}

	public function getAuthor($name) {
		$resultSet = $this->db->selectAuthor($name);
		$author = new Author($resultSet[0]['Author_ID'], $resultSet[0]['Author_Name']);
		return $author;
	}

	public function getAllRecipes() {
		$resultSet = $this->db->selectAllAuthors();
		$authors = array();
		foreach ($resultSet as $key => $value) {
			$auth = $value;

			$recipes = $this->db->selectRecipeForAuthor($auth['Author_ID']);
			$auth['recipes'] = $recipes;

			array_push($authors, $auth);
		}

		return $authors;
	}

	public function getRecipe($name) {
		$resultSet = $this->db->selectRecipe($name);
		$recipe = new Recipe($resultSet[0]['Recipe_ID'], $resultSet[0]['Recipe_Author_ID'], $resultSet[0]['Recipe_Ingredients'], $resultSet[0]['Recipe_Instructions'], $resultSet[0]['Recipe_Name']);
		return $recipe;
	}

	public function insertAuthor($id, $name) {
		$affectedRows = $this->db->insertAuthor($id, $name);
		return $affectedRows;
	}

	public function insertRecipe($aid, $ing, $ins, $name) {
		$affectedRows = $this->db->insertRecipe($aid, $ing, $ins, $name);
		return $affectedRows;
	}

	public function deleteAuthor($id) {
		$affectedRows = $this->db->deleteAuthor($id);
		return $affectedRows;
	}

	public function deleteRecipe($id) {
		$affectedRows = $this->db->deleteRecipe($id);
		return $affectedRows;
	}

	public function updateAuthor($id, $name) {
		$affectedRows = $this->db->updateAuthor($id, $name);
		return $affectedRows;
	}

	public function updateRecipe($id, $aid, $ing, $ins, $name) {
		$affectedRows = $this->db->updateRecipe($id, $aid, $ing, $ins, $name);
		return $affectedRows;
	}

	public function filterRecipes($filter) {
		$resultSet = $this->db->filterRecipes($filter);
		return $resultSet;
	}
}


?>