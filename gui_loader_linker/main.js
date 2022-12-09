let button = document.getElementById('mybtn');
let removeButton = document.getElementById('removebtn');
const parent = document.getElementsByClassName("parent");
const table = document.getElementsByClassName("design");
const message = document.getElementById("message");

// when click on Generate
button.onclick = async () => {
    
    // delete  dataframe if it exists

    message.innerHTML = '';
    // if(parent[0].firstElementChild)
    //     parent[0].removeChild(table[0]);
        
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

    if(progType == 'SICXE' && stAddr.value == ''){
        console.log('==')
        var text = document.createTextNode( 'You should put start Address');
        message.appendChild(text);
        console.log(message)
        return;
    }
    formData.append('text' , text);
    formData.append('type', progType);
    formData.append('address' , stAddr.value? stAddr.value: '');
    await fetch('http://localhost:5000/inputs', {
        'method' : 'POST',
        'body': formData
    }).then(response => response.json())
    .then(response => console.log(response))
    
} 


// remove btn
removeButton.onclick = () => {
    message.innerHTML = '';
    const parent = document.getElementsByClassName("parent");
    const table = document.getElementsByClassName("table");

    if(parent[0].firstElementChild)
        parent[0].removeChild(table[0]);
    
}