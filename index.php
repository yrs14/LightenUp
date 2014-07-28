<!DOCTYPE html>
<html>
    <head>
        <title>Fat Check</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        
    </head>
    <body>
        <div>
            
            <form action="insert_data.php" method="POST">
                <label for="height">Height</label>
                <input type="text" id="height" name="height"/> <br /><br />
                
                <label for="weight">Weight</label>
                <input type="text" id="weight" name="weight"/> <br /><br />
                
                <label for="age">Age</label> <!-- dropdown list -->
                <input type="text" id="age" name="age" />
                
                <label for="gender">Gender</label> <!-- radio button? -->
                <select id="gender" name="gender">
                    <option>Male</option>
                    <option>Female</option>
                </select> <br /><br />
                
                <input type="submit" name="submitButton" id="submitButton" />
            </form>    

            
        </div>
    </body>
</html>
