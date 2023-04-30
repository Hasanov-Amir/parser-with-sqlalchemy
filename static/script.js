fetch('http://127.0.0.1:8080/show_changes')
      .then(response => response.json())
      .then(json => console.log(json))
