
//all html files are linked to this file to enable search functionality
//handle click events on search button and clickable divs (top 3 items and search results)
function search_input_string(input_string){
    if(input_string != ''){
        window.location.replace("http://127.0.0.1:5000/search/" + input_string);
    }else{
        $(".search-box").val('');
        $(".search-box").focus()
    }
}

function view_item_by_id(id){
    $(".search-box").focus();
    if(id){
        window.location.replace("http://127.0.0.1:5000/view/" + id);
    }else{
        console.log("item does not exist")
    }
  
}

$(document).ready(function() {
    //focus on the search box
    $(".search-box").focus();
    
    //remove any display
    $('.matched-item-div').empty();

    // //firing submit event on a form 
    // //must use event.preventDefault() otherwise redirecting won't work
    // $("#navbar-search-btn").submit(function(event){
    //     event.preventDefault();
        
    // })

    $("#navbar-search-btn").click(function(event){
        event.preventDefault();
        let input_string = $('.search-box').val();
        search_input_string(input_string);
        // //debugging
        // console.log("here")
        // console.log(input_string);
    })
    

    //only work if in main.html and search.html has a script all the way to the top 
    //that link to main.js and display_search_result.js first 
    //because .clickable-div is created dynamically in those js files
    $(".clickable-div").click(function(){
        
        let extracted_id = parseInt($(this).attr("id"))
        view_item_by_id(extracted_id)

        // //debugging
        // console.log("here main")
        // console.log(extracted_id)
        
    })

})

