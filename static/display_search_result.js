function display_items(match_items){
    // remove all items
    $('.matched-item-div').empty();
    if(match_items.length == 0){
        let $newDiv = $("<div>").addClass("my-3 matched-items")
        let $childDiv = $("<div> Results Not Found </div>")
        
        //newDiv add itemDiv first 
        $newDiv.append($childDiv)
        $('.match-item-div').append($newDiv)
    }
    $.each(match_items, function(key, value){
        //if the item has an id, add it to the class
        if(value["id"]){
            let id = value["id"].toString()     

            let $newDiv = $("<div>").addClass("mt-4 matched-items clickable-div")
                                    .attr('id', id) 
                                    .append($("<hr>"))

           
                        
            let $titleDiv = $("<div>" + value["title"] + "</div>")
                            .addClass("medium-size-title")

            let $classID =  $('<div><span class="class-label pt-5">Class ID: </span>'+ value["class_id"]+'</div>') 

            let $className =  $('<div><span class="class-label pt-5">Class Name: </span>'+ value["class_name"]+'</div>')

            let $profName =  $('<div><span class="class-label pt-5">Professor(s): </span>'+ value["professors"]+'</div>')

            let $imgDiv = $('<img>')
                            .attr({'src': value["cover_image"], 'width':70, 'height': 'auto', 'alt':"cover image"})
                            .addClass("mt-2")
            ////newDiv add itemDiv first 
            $newDiv.append($titleDiv, $classID,$className,$profName,$imgDiv)
            $('.match-item-div').append($newDiv)
        }
    })
}


$(document).ready(function() {
    display_items(match_items);
})