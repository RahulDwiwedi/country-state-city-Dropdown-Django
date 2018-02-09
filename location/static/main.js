function getState(countryId) { 
var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("statediv").innerHTML = this.responseText;
    }
  };
   xhttp.open("GET", "/country/"+countryId, true);
  xhttp.send();
}

function getCity(stateId) { 
var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("citydiv").innerHTML = this.responseText;
    }
  };
   xhttp.open("GET", "/state/"+stateId, true);
  xhttp.send();
}


$(document).on('submit','#locationform',function(e){
	e.preventDefault();
	
});

function result(){
var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("result").innerHTML = this.responseText;
    }
  };
   xhttp.open("GET", "/".concat($('select[name=country]').val(),"/",$('select[name=state]').val(),"/",$('select[name=city]').val()), true);
  xhttp.send();
}
