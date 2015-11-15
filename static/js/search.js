function search(e, url) {
    var search_input = document.getElementById('search');

    if (e.keyCode == 13) {
        window.location.href = url + search_input.value
    }
}