<?php
/* Simple Country - Region Selector
 *
 *	Author : Viki (a) Vignesh Natarajan
 *	Firma  : viklabs.org
 */	


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bug Report</title>
    <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        }

        td, th {
        border: 1px solid #868686;
        text-align: left;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
        

	div.right{
	  float:right;
	  padding-right: 100px;	
	}
    </style>
</head>
<body>

  <div>
    <h2>Country & City</h2>
    <div>
	<p>
        <label for="region_name">Region Name </label>
        <select name="region_name" id="region_name"  onchange="region_select_action.call(this, event)">
        </select>
	</p>

	<p>
        <label for="municipal_name">Minicipality Name </label>
        <select name="municipal_name" id="municipal_name">
        </select>
	</p>
    </div>

<script>

/*
function load_city_list(){
	const json_file = 'https://bugs.vikilabs.org/city_list.json';
	let dropdown = document.getElementById('municipal_name');
	let default_option = document.createElement('option');
	default_option.text = 'Choose Municipality';
	dropdown.length = 0;
	dropdown.selectedIndex = 0;

	dropdown.add(default_option);
	
	const request = new XMLHttpRequest();
	request.open('GET', json_file, true);

	request.onload = function() {
		if (request.status != 200) {
			console.log("unable to read json file "+json_file);
			return;
		}

		const data = JSON.parse(request.responseText);
		let option;

		for (let i = 0; i < data.length; i++) {
			option = document.createElement('option');
			//console.log(data[i]);
			option.text = data[i];
			option.value = data[i];
			dropdown.add(option);
		}
	}

	request.onerror = function() {
  		console.error('unable to read json file ' + json_file);
	};

	request.send();
}
*/

function load_region_list(){
	const json_file = 'https://bugs.vikilabs.org/region_list.json';
	let dropdown = document.getElementById('region_name');
	let default_option = document.createElement('option');
	default_option.text = 'Choose Region';
	dropdown.length = 0;
	dropdown.selectedIndex = 0;


	let mdropdown = document.getElementById('municipal_name');
	let mdefault_option = document.createElement('option');
	mdefault_option.text = 'Choose Municipality';
	mdropdown.length = 0;
	mdropdown.selectedIndex = 0;


	dropdown.add(default_option);
	
	const request = new XMLHttpRequest();
	request.open('GET', json_file, true);

	request.onload = function() {
		if (request.status != 200) {
			console.log("unable to read json file "+json_file);
			return;
		}

		const data = JSON.parse(request.responseText);
		let option;

		for (let i = 0; i < data.length; i++) {
			option = document.createElement('option');
			//console.log(data[i]);
			option.text = data[i];
			option.value = data[i];
			dropdown.add(option);
		}
	}

	request.onerror = function() {
  		console.error('unable to read json file ' + json_file);
	};

	request.send();
}

function region_select_action(event)
{
	var selected_region = this.options[this.selectedIndex].text;
	const json_file = 'https://bugs.vikilabs.org/region_city_mapping.json';
	let dropdown = document.getElementById('municipal_name');
	let default_option = document.createElement('option');
	default_option.text = 'Choose Municipality';
	dropdown.length = 0;
	dropdown.selectedIndex = 0;

	dropdown.add(default_option);

	const request = new XMLHttpRequest();
	request.open('GET', json_file, true);

	request.onreadystatechange= function() {
		if (request.status != 200) {
			console.log("unable to read json file "+json_file);
			return false;
		}
	
		const data = JSON.parse(request.responseText);


		var city_list = data[selected_region];
		
		console.log(city_list);

		let option;
		for (let i = 0; i < city_list.length; i++) {
			option = document.createElement('option');
			option.text = city_list[i];
			option.value = city_list[i];
			dropdown.add(option);
		}
	}

	request.onerror = function() {
		console.error('unable to read json file ' + json_file);
	};

	request.send();
}

//load_city_list();
load_region_list();
</script>

</body>
</html>

