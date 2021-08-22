var filteredResult = new Array();

function showAuthor(user) {
	var content = "Author_ID: " + user.Author_ID + "<br/>" +
				  "Author_Name: " + user.Author_Name + "<br/>";
	$("#main").html(content);
}

function showRecipe(user) {
	var content = "Recipe_ID: " + user.Recipe_ID + "<br/>" +
				  "Recipe_Author_ID: " + user.Recipe_Author_ID + "<br/>" +
				  "Recipe_Ingredients: " + user.Recipe_Ingredients + "<br/>" +
				  "Recipe_Instructions: " + user.Recipe_Instructions + "<br/>" +
				  "Recipe_Name: " + user.Recipe_Name + "<br/>";
	$("#main").html(content);
}

function showResult(rows) {
	var content = "Affected rows: " + rows;
	$("#main").html(content);
}

function showFilters(recipes) {
	var content = "<table><thead><tr><td>Recipe Name</td><td>Recipe Instructions</td><td><Recipe Ingredients>Recipe Ingredients</td></tr></thead>"
	console.log(recipes);
	i = 0;
	recipes.forEach(elem => {
			recipe = elem;
			if (i % 2 == 0) {
				content += "<tr class='mytablerow'>";
			} else {
				content += "<tr class='mytablerow2'>";
			}
			i++;
			content += "<td>" + recipe.Recipe_Name + "</td>" +
					   "<td>" + recipe.Recipe_Instructions + "</td>" +
					   "<td>" + recipe.Recipe_Ingredients + "</td>" +
					   "<td>";
			content += "</td></tr>";
	});
	content += "</table>";
	filteredResult.push($('#filRecipe').val());
	var options = document.getElementById("opts");
	while (options.hasChildNodes()) {
		options.removeChild(options.firstChild);
	}
	for (var i = 0; i < filteredResult.length - 1; i++) {
		var option_var = document.createElement("option");
		option_var.setAttribute("value", filteredResult[i]);
		var context = document.createTextNode(filteredResult[i]);
		option_var.appendChild(context);
		options.appendChild(option_var);	
	}
	$("#main").html(content);
}

function showAllRecipes(recipes) {
	var content = "<table><thead><tr><td>Author_ID</td><td>Author_Name</td><td>Recipes</td></tr></thead>";
	console.log(recipes);
	i = 0;
	recipes.forEach(elem => {
			author = elem;
			if (i % 2 == 0) {
				content += "<tr class='mytablerow'>";
			} else {
				content += "<tr>";
			}
			i++;
			content += "<td>" + author.Author_ID + "</td>" +
					   "<td>" + author.Author_Name + "</td>" +
					   "<td>";
			author.recipes.forEach(recipe => {
				content += "Recipe Name: " + recipe.Recipe_Name + ", Recipe_Instructions: " + recipe.Recipe_Instructions + ", Recipe_Ingredients: " + recipe.Recipe_Ingredients + " <br/> ";
			});
			content += "</td></tr>";
	});
	content += "</table>";

	$("#main").html(content);
}

$(document).ready(function() {
	$("#btn_getAuthor").click(function() {
		$.getJSON(
			"./controller/controller.php",  
			{ action: "getAuthor", user: $('#author').val() }, 
			showAuthor
		);
	});

	$("#btn_getRecipe").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "getRecipe", user: $('#recipe').val() },
			showRecipe
		);
	});

	$("#btn_getRecipes").click(function() {
		$.getJSON(
			"./controller/controller.php",  
			{ action: "getAllRecipes" }, 
			showAllRecipes
		);
	});

	$("#btn_addAuthor").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "insertAuthor", authorID: $('#authorID').val(), authorName: $('#authorName').val() },
			showResult
		);
	});

	$("#btn_addRecipe").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "insertRecipe", aid: $('#recipeAuthorID').val(), ing: $('#recipeIngredients').val(), ins: $('#recipeInstructions').val(), name: $('#recipeName').val() },
			showResult
		);
	});

	$("#btn_deleteAuthor").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "deleteAuthor", authorID: $('#delAuthorID').val() },
			showResult
		);
	});

	$("#btn_deleteRecipe").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "deleteRecipe", recipeID: $('#delRecipeID').val() },
			showResult
		);
	});

	$("#btn_updateAuthor").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "updateAuthor", authorID: $('#updAuthorID').val() , authorName: $('#updAuthorName').val() },
			showResult
		);
	});

	$("#btn_updateRecipe").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "updateRecipe", id: $('#updRecipeID').val(), aid: $('#updRecipeAuthorID').val(), ing: $('#updRecipeIng').val(), ins: $('#updRecipeIns').val(), name: $('#updRecipeName').val() },
			showResult
		);
	});

	$("#btn_filterRecipes").click(function() {
		$.getJSON(
			"./controller/controller.php",
			{ action: "filterRecipes", filter: $('#filRecipe').val() },
			showFilters
		);
	})
});