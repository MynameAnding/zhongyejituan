(function (global, factory) {
  if (typeof define === "function" && define.amd) {
    define([], factory);
  } else if (typeof exports !== "undefined") {
    factory();
  } else {
    var mod = {
      exports: {}
    };
    factory();
    global.bootstrapTableZhCN = mod.exports;
  }
})(this, function () {
  'use strict';

  /**
   * Bootstrap Table Chinese translation
   * Author: Zhixin Wen<wenzhixin2010@gmail.com>
   */
  (function ($) {
    $.fn.bootstrapTable.locales['zh-CN'] = {
      formatLoadingMessage: function formatLoadingMessage() {
        return '\u6b63\u5728\u52aa\u529b\u5730\u52a0\u8f7d\u6570\u636e\u4e2d\uff0c\u8bf7\u7a0d\u5019\u002e\u002e\u002e';//正在努力的加载中，请稍等。。。
      },
      formatRecordsPerPage: function formatRecordsPerPage(pageNumber) {
        return pageNumber;
      },
      formatShowingRows: function formatShowingRows(pageFrom, pageTo, totalRows) {
        return '\u5171\u6709' + totalRows + '\u884c';
      },
      formatDetailPagination: function formatDetailPagination(totalRows) {
        return totalRows;
      },
      formatSearch: function formatSearch() {
        return '\u641c\u7d22\u002e\u002e\u002e';
      },
      formatNoMatches: function formatNoMatches() {
        return '\u6ca1\u6709\u627e\u5230\u5339\u914d\u7684\u8bb0\u5f55';
      },
      formatPaginationSwitch: function formatPaginationSwitch() {
        return '\u9690\u85cf\u002f\u663e\u793a\u5206\u9875';
      },
      formatRefresh: function formatRefresh() {
        return '\u5237\u65b0';
      },
      formatToggle: function formatToggle() {
        return '\u5207\u6362';
      },
      formatColumns: function formatColumns() {
        return '\u9009\u62e9\u5c55\u793a\u5217';
      },
      formatFullscreen: function formatFullscreen() {
        return '\u5168\u5c4f';
      },
      formatAllRows: function formatAllRows() {
        return '\u6240\u6709';
      },
      formatAutoRefresh: function formatAutoRefresh() {
        return '\u81ea\u52a8\u5237\u65b0';
      },
      formatExport: function formatExport() {
        return '\u5bfc\u51fa\u6570\u636e';
      },
      formatClearFilters: function formatClearFilters() {
        return '\u6e05\u7a7a\u8fc7\u6ee4';
      },
      formatJumpto: function formatJumpto() {
        return '\u8df3\u8f6c';
      },
      formatAdvancedSearch: function formatAdvancedSearch() {
        return '\u9ad8\u7ea7\u641c\u7d22';
      },
      formatAdvancedCloseButton: function formatAdvancedCloseButton() {
        return '\u5173\u95ed';
      }
    };

    $.extend($.fn.bootstrapTable.defaults, $.fn.bootstrapTable.locales['zh-CN']);
  })(jQuery);
});