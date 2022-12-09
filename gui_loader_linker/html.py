
html_str = '''
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIC/SICXE LOADER-LINKER</title>

    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">  
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="main_screen">
        <div class="container">
            <h1 style="color:white" >SIC/SICXE Loader_Linker</h1>
            <div class="first">
             <div class="input-group" style="width: 30%">
                <input type="file"  id = "myfile" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload">
              </div>
            </div>
           <div class="sec" style = "width:20%; cursor:pointer">
              <select class="form-select" aria-label="Default select example" id= "language">
                <option value="SIC">SIC</option>
                <option value="SICXE">SICXE</option>
              </select>
            </div>
            <div class="col-2 third" style = "width:20%">
                <input type="text" id = "address" class="form-control" placeholder="Enter the address" aria-label="Zip">
              </div>
              <div class = "buttons">
              <button type="button" id = "removebtn" class="btn btn-primary btn-lg">Remove</button>
              <button type="button" id = "mybtn" class="btn btn-secondary btn-lg">Generate</button>
            </div>
            <p id = "message"></p>
            <div class = "parent">
            {table}
            </div>
            </div>
    </div>
</body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script type="text/javascript"src="main.js"></script>
</html>
'''