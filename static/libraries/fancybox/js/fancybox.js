// Customize icons
$.fancybox.defaults = $.extend(true, {}, $.fancybox.defaults, {

  // Class for adding custom css
  baseClass: "fancybox-custom-layout",

  // Should display toolbar (buttons at the top)
  // Can be true, false, "auto"
  // If "auto" - will be automatically hidden if "smallBtn" is enabled
  toolbar: "true",

  // Enabling Fancybox features btns
  buttons: [
    "close",
    "thumbs",
    "slideShow",
    "zoom",
    "fullScreen",
    "share",
    "download"
  ],

  // Custom icons
  btnTpl: {
    arrowLeft: '<button data-fancybox-prev class="fancybox-button fancybox-button--arrow_left" title="{{PREV}}">' +
      '<div><i class="fal fa-arrow-left"></i></div>' +
      "</button>",

    arrowRight: '<button data-fancybox-next class="fancybox-button fancybox-button--arrow_right" title="{{NEXT}}">' +
      '<div><i class="fal fa-arrow-right"></i></div>' +
      "</button>",

    close: '<button data-fancybox-close class="fancybox-button fancybox-button--close" title="{{CLOSE}}">' +
      '<i class="fal fa-times"></i>' +
      "</button>",

    thumbs: '<button data-fancybox-thumbs class="fancybox-button fancybox-button--thumbs" title="{{THUMBS}}">' +
      '<i class="fal fa-th-large"></i>' +
      "</button>",

    slideShow: '<button data-fancybox-play class="fancybox-button fancybox-button--play" title="{{PLAY_START}}">' +
      '<i class="fal fa-play"></i>' +
      '<i class="fal fa-pause"></i>' +
      "</button>",

    download: '<a download data-fancybox-download class="fancybox-button fancybox-button--download ml-lg-1 ml-md-1" title="{{DOWNLOAD}}" href="javascript:;">' +
      '<i class="fal fa-download"></i>' +
      "</a>",

    zoom: '<button data-fancybox-zoom class="fancybox-button fancybox-button--zoom" title="{{ZOOM}}">' +
      '<i class="fal fa-search"></i>' +
      "</button>",

    fullScreen: '<button data-fancybox-fullscreen class="fancybox-button fancybox-button--fsenter" title="{{FULL_SCREEN}}">' +
      '<i class="fal fa-expand"></i>' +
      '<i class="fal fa-compress"></i>' +
      "</button>",

    share: '<button data-fancybox-share class="fancybox-button fancybox-button--share" title="{{SHARE}}">' +
      '<i class="fal fa-share"></i>' +
      "</button>"
  }
});