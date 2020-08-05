
function Edit(elm) {
    alert('edit!')
    $.ajax({
        url: '/movies/$(elm.slug)/edit_movie',
        data: $('form').serialize(),
        type: 'POST',
        success: function(res) {
            console.log(res);
            
        },
        error: function(error) {
            console.log(error);
           
        }
    });
}