let button = document.getElementById('mybtn');


// when click on Generate
button.onclick = async () => {
    
    // delete  dataframe if it exists
    const parent = document.getElementsByClassName("parent");
    const table = document.getElementsByClassName("design");
    console.log(parent)
    if(parent.childElementCount > 0)
        parent.removeChild(table);
        
    // take the inputs
    let specify = document.getElementById("language");
    let progType = specify.value;
    console.log(progType)
        // select file
    const selectedFile = document.getElementById('myfile').files[0]
    text = await selectedFile.text();
    const formData = new FormData();
        // start address
    const stAddr = document.getElementById('address');

    formData.append('text' , text);
    formData.append('type', progType);
    formData.append('address' , stAddr.value? stAddr.value: '');
    await fetch('http://localhost:5000/inputs', {
        'method' : 'POST',
        'body': formData
    }).then(response => response.json())
    .then(response => console.log(response))
    
} 
