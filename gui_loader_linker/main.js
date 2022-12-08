let button = document.getElementById('mybtn');


// when click on Generate
button.onclick = async () => {
    
    // delete  dataframe if it exists
    const table = document.getElementsByClassName("table");
    // console.log(table)
    if(table != null && table.length > 0) {
        table.remove();
    }
        
    // take the inputs
    let specify = document.getElementById("language");
    let progType = specify.value;
    console.log(progType)
        // select file
    const selectedFile = document.getElementById('myfile').files[0]
    text = await selectedFile.text();
    console.log(text)

    await fetch('http://localhost:5000/inputs', {
        method: 'POST',
        body: JSON.stringify(text),
        mode: 'cors', // no-cors, *cors, same-origin
        }).then(
            response => response.json()// if the response is a JSON object
          ).catch((error) => {
            console.log(error);
        })  
  
} 
