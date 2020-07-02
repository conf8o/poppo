$(() => {
    $.get('https://holidays-jp.github.io/api/v1/date.json', function(holidays) {
        $("td").each(function(i, element) {
            const $element = $(element);
            console.log(holidays[$element.attr('id')]);
            if (holidays[$element.attr('id')]) {
                $element.addClass('holiday');
            }
        });
    });
});