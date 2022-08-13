

//display 3 most popular items 
function display_popular_items(textbooks){
    // remove all items
    $('#popular-items-row').empty();
    $.each(textbooks, function(key, value){
        // console.log(value["title"])

        let $newDiv = $("<div>").addClass("col-sm-auto mb-5 top-items")
                                
                    
        let $titleDiv = $('<div class="row mb-2"></div>').append(
                            $('<div class="col-sm-auto"></div>').append(
                                $('<div class="title">' +value["title"]+ '</div>')
                            )
                        )

        let $imageAndDetailsDiv = $('<div class="row"></div>').append(
            $('<div class="col-sm-auto clickable-div"></div>').append(
                $('<img>')
                    .attr({'src': value["cover_image"], 'width':80, 'height': 'auto', 'alt': "cover image"})
                    
            ).attr('id', key+1),
            $('<div class="col-sm-6"></div>').append(
                // $('<div class="title mb-1">' +value["title"]+ '</div>'),
                $('<div class="description-summary">'+ value["description"] +'</div>'),
                // $('<button type="button" class="btn btn-outline-info btn-sm mt-1"><span class="class-label mr-3">'+ value["class_id"]+'</span></button>')

                $('<div class="cursor-default"><span class="class-label pt-5">Class ID: </span>'+ value["class_id"]+'</div>'),
                // $('<div><span class="label-text mr-3">Class Name:   </span>'+ value["class_name"] +'</div>'),
                // $('<div><span class="label-text mr-3">Professors:   </span>'+ value["professors"] +'</div>')
                    
            ),
        )
                            
        // let $childDiv = $("<div>" +value["title"]+ "</div>")
        // let $coverImage = $("<img>")
        //                         .attr({'src': value["cover_image"], 'width':80, 'height': 'auto'})
        // let classDetail = $("<span> </span>")
                                

        $newDiv.append($titleDiv, $imageAndDetailsDiv)
        $('#popular-items-row').append($newDiv)
        
    })

}



$(document).ready(function() {
    //focus on the search box
    $(".search-box").focus()
     
    //display the popular items
    display_popular_items(textbooks);

    
})
