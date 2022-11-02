document.getElementById('search_pole').addEventListener('keyup', function (event) {
        document.getElementById('searchBtn').href = "/goods/search/" + document.getElementById(
            'search_pole').value;
        if (event.keyCode == 13) {
            document.getElementById('searchBtn').click();
        }
    });

    document.getElementById('search_pole1').addEventListener('keyup', function (event) {
        document.getElementById('searchBtn1').href = "/goods/search/" + document.getElementById(
            'search_pole1').value;
        if (event.keyCode == 13) {
            document.getElementById('searchBtn1').click();
        }
    });