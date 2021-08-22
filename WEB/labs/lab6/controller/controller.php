<?php


require_once '../model/model.php';
require_once '../view/view.php';

class Controller {
	private $view;
	private $model;

	public function __construct() {
		$this->model = new Model();
		$this->view = new View();
	}

	public function service() {
		if (isset($_GET['action']) && !empty($_GET['action'])) {
			switch ($_GET['action']) {
				case "getAuthor":
					$this->{$_GET['action']}($_GET['user']);
					break;
				case "getRecipe":
					$this->{$_GET['action']}($_GET['user']);
					break;
				case "insertAuthor":
					$this->{$_GET['action']}($_GET['authorID'], $_GET['authorName']);
					break;
				case "insertRecipe":
					$this->{$_GET['action']}($_GET['aid'], $_GET['ing'], $_GET['ins'], $_GET['name']);
					break;
				case "deleteAuthor":
					$this->{$_GET['action']}($_GET['authorID']);
					break;
				case "deleteRecipe":
					$this->{$_GET['action']}($_GET['recipeID']);
					break;
				case "updateAuthor":
					$this->{$_GET['action']}($_GET['authorID'], $_GET['authorName']);
					break;
				case "updateRecipe":
					$this->{$_GET['action']}($_GET['id'], $_GET['aid'], $_GET['ing'], $_GET['ins'], $_GET['name']);
					break;
				case "filterRecipes":
					$this->{$_GET['action']}($_GET['filter']);
					break;
				default:
					$this->{$_GET['action']}();
					break;
			}
	   }
	}

	public function getAuthor($name) {
		$author = $this->model->getAuthor($name);
		return $this->view->output($author);
	}

	public function getRecipe($name) {
		$recipe = $this->model->getRecipe($name);
		return $this->view->output($recipe);
	}

	public function getAllRecipes() {
		$recipes = $this->model->getAllRecipes();
		return $this->view->output($recipes);
	}

	public function insertAuthor($id, $name) {
		$affectedRows = $this->model->insertAuthor($id, $name);
		return $this->view->output($affectedRows);
	}

	public function insertRecipe($aid, $ing, $ins, $name) {
		$affectedRows = $this->model->insertRecipe($aid, $ing, $ins, $name);
		return $this->view->output($affectedRows);
	}

	public function deleteAuthor($id) {
		$affectedRows = $this->model->deleteAuthor($id);
		return $this->view->output($affectedRows);
	}

	public function deleteRecipe($id) {
		$affectedRows = $this->model->deleteRecipe($id);
		return $this->view->output($affectedRows);
	}

	public function updateAuthor($id, $name) {
		$affectedRows = $this->model->updateAuthor($id, $name);
		return $this->view->output($affectedRows);
	}

	public function updateRecipe($id, $aid, $ing, $ins, $name) {
		$affectedRows = $this->model->updateRecipe($id, $aid, $ing, $ins, $name);
		return $this->view->output($affectedRows);
	}

	public function filterRecipes($filter) {
		$recipes = $this->model->filterRecipes($filter);
		return $this->view->output($recipes);
	}
}

$controller = new Controller();
$controller->service();

?>