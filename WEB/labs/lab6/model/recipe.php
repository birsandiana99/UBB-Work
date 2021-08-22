<?php


class Recipe implements JsonSerializable {
	private $Recipe_ID;
	private $Recipe_Author_ID;
	private $Recipe_Ingredients;
	private $Recipe_Instructions;
	private $Recipe_Name;

	public function __construct($id, $aid, $ing, $ins, $name) {
		$this->Recipe_ID = $id;
		$this->Recipe_Author_ID = $aid;
		$this->Recipe_Ingredients = $ing;
		$this->Recipe_Instructions = $ins;
		$this->Recipe_Name = $name;
	}

	public function getId() {
		return $this->Recipe_ID;
	}

	public function getAId() {
		return $this->Recipe_Author_ID;
	}

	public function getIng() {
		return $this->Recipe_Ingredients;
	}

	public function getIns() {
		return $this->Recipe_Instructions;
	}

	public function getName() {
		return $this->Recipe_Name;
	}

	public function jsonSerialize() {
		$vars = get_object_vars($this);
		return $vars;
	}
}


?>