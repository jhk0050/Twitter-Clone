///////////////////
/// Javascript for posts page
/////////////////////////

$(function() {
    //// executed when js-menu-icon menu clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.js.menu
        // toggle() : switch show and hide
        $(this).next().toggle();

    })
})