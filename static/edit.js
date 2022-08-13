$(document).ready(function(){
    
    //pre-populate the form base on the data from id
    $('#title').val(data["title"])
    $('#cover_image').val(data["cover_image"])
    
    $.each(data["authors"], function(index, value){
        $.each(value, function(i, v){
            if (i == "fl"){
                $('#authors').val(v)
            }
        })
       
    })

    $('input[name=rating][value=' + data["rating"] + ']').prop('checked',true)
    $('#description').val(data["description"])
    $('#class_id').val(data["class_id"])
    $('#class_name').val(data["class_name"])
    $('input[name=required_reading][value=' + data["required_reading"].toLowerCase() + ']').prop('checked',true)
    
    $.each(data["professors"], function(index, value){
        $('#professors').val(value)
       
    })
    
    $.each(data["tags"], function(index, value){
        $('#tags').val(value)
       
    })
    
    // console.log(data)

    // Discard button handling 
    $('#edit-textbook-discard-btn').click(function(event){
        event.preventDefault()
        let isDiscard = confirm("Are you sure? Content won't be saved.")
        alert(isDiscard);
        if(isDiscard){
            window.location.replace("http://127.0.0.1:5000/view/"+id);
        }else{
            $('input:text[value=""],textarea:empty').first().focus();
        }
    })
    
    
    //validate the form 
    $('#edit-textbook-form').validate({
        //source: https://stackoverflow.com/questions/10111907/how-to-focus-invalid-fields-with-jquery-validate
        onfocusout: false,
        invalidHandler: function(form, validator) {
             var errors = validator.numberOfInvalids();
            if (errors) {                    
                validator.errorList[0].element.focus();
            }
        },
        // source: https://stackoverflow.com/questions/14913677/jquery-validation-plugin-message-style
        errorPlacement: function(label, element){
            //invalid-feedback is a bootstrap class
            label.addClass('invalid-feedback')
            label.insertBefore(element)
        },
        wrapper:'div'

        
    });

    //focus on invalid element
    $("#validate").click(function() {
        if ($("#test-form").valid()) 
              alert("Valid!");
        else
              validator.focusInvalid();

        return false;
    });

    $('#edit-textbook-form').addClass("was-validated")

    $('#edit-textbook-submit-btn').submit(function(event){
        event.preventDefault()
        window.location.replace("http://127.0.0.1:5000/edit/1" );

    })

})
