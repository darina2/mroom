
function Edit(elm) {
    alert('edit!')
    $.ajax({
        url: '/movies/$(elm.slug)/edit_movie',
        data: $('form').serialize(),
        type: 'POST',
        success: function(res) {
            console.log(res);
            alert('success!')
            alert(status)
            alert(res)
        },
        error: function(error) {
            console.log(error);
            alert('nit success!')
            alert(status)
            alert(error)
        }
    });
}