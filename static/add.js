
//Display success response if submitted
function display_submit_response(){
    $('#submit-response').empty()

    let newDivTitle = '<div class="row justify-content-center align-items-center mt-5" id="response-title">\
                            <div class="col-sm-auto">\
                                <h1>New textbook successfully created!</h1>\
                            </div>\
                        </div>' 
    let newDivButton = '<div class="row justify-content-center align-items-center mt-2">\
                            <div class="col-sm-auto">\
                                <button class="btn btn-info submit-btn" id="add-more-btn" type="submit">Add More</button>\
                            </div>\
                            <div class="col-sm-auto">\
                                <button class="btn btn-info submit-btn" id="view-item-btn"  type="submit">View Item</button>\
                            </div>\
                        </div>'



    $('#submit-response').append(newDivTitle, newDivButton)
}


$(document).ready(function(){

    $('#title').focus();

    //validate the form 
   
    $('#add-textbook-form').validate({
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


    //when form is submit, users can view the item or add more item 
    $("#add-textbook-submit-btn").click(function(event){

        event.preventDefault();

        // was-validated is a bootstrap class
        $('#add-textbook-form').addClass("was-validated")

        //check if the form is valid
        let isValid =  $('#add-textbook-form').valid()

        // console.log(isValid)
        if (isValid){
            let formData = {
                'title' : $('#title').val(),
                'cover_image': $('#cover_image').val(), 
                'authors' : $('#authors').val(),
                'rating': $('input[name="rating"]:checked').val(),
                'description': $.trim($('#description').val()),
                'class_id' : $('#class_id').val(),
                'class_name' : $('#class_name').val(),
                'required_reading': $('input[name="required_reading"]:checked').val(),
                'professors' : $('#professors').val(),
                'tags': $('#tags').val()
            }
            // console.log(formData)

            $.ajax({
                type: "POST",
                url: "add_result",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify(formData),
                success: function(result){
                    let new_data = result["new_data"]
                    data = new_data
                    //fix reset state
                    $('#add-textbook-form').removeClass("was-validated")
                    $('#add-textbook-form').trigger("reset");
                    $('#title').focus()
                    // console.log("here")
                    // console.log(data)
                    display_submit_response()
                    id = data["id"] 
                    $('#view-item-btn').click(function(e){
                        e.preventDefault();
                        window.location.replace("http://127.0.0.1:5000/view/"+id);
                    })

                    $('#add-more-btn').click(function(e){
                        e.preventDefault();
                        window.location.replace("http://127.0.0.1:5000/add");
                    })
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            })
        }else{
            validator.focusInvalid();
        }
    })

    


})