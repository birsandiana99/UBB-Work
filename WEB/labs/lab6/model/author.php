<?php


class Author implements JsonSerializable {
	private $Author_ID;
	private $Author_Name;

	public function __construct($id, $name) {
		$this->Author_ID = $id;
		$this->Author_Name = $name;
	}

	public function getId() {
		return $this->Author_ID;
	}

	public function getName() {
		return $this->Author_Name;
	}

	public function JsonSerialize() {
		$vars = get_object_vars($this);
		return $vars;
	}
}


?>