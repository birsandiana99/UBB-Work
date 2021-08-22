<?php


require_once '../model/author.php';
require_once '../model/recipe.php';

class View {
	public function __construct() {}

	public function outputAuthor($author) {
		echo json_encode($author);
	}

	public function outputRecipe($recipe) {
		echo json_encode($recipe);
	}

	public function output($param) {
		echo json_encode($param);
	}
}


?>