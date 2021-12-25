const loadObjects = [];

function imageLoad(div) {
    loadObjects.push({'div': div});
    const index = loadObjects.length - 1;
    window.setTimeout('imageLoadTimeout(' + index + ')', 100);
}

function imageLoadTimeout(index) {
    const loadObject = loadObjects[index];
    $('<img src="' + loadObject.div.attr("data") + '" alt="Heiko Schmidt">').on('load', function () {
        loadObject.div.prop('src', loadObject.div.attr('data'));
        $(this).remove();
        loadObjects[index] = null;
    });
}

$(function () {
    imageLoad($('#photo'));
});
