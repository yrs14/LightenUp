<!DOCTYPE html>
<html>
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("#div1").fadeIn();
});
</script>
        <title id="title">Fat Check</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    </head>
    <body>
        <div>
            
            <form action="insert_data.php" method="POST">
                <label for="height" class="enter">Height</label>
                <input type="text" id="height" name="height"/> <br /><br />
                
                <label for="weight" class="enter">Weight</label>
                <input type="text" id="weight" name="weight"/> <br /><br />
                
                <label for="age" class="enter">Age</label> <!-- dropdown list -->
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
