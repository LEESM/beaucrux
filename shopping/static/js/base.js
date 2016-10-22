function rudr_favorite(a) {
  pageTitle=document.title;
  pageURL=document.location;
  try {
    // Internet Explorer solution
    eval("window.external.AddFa-vorite(pageURL, pageTitle)".replace(/-/g,''));
  }
  catch (e) {
    try {
      // Mozilla Firefox solution
      window.sidebar.addPanel(pageTitle, pageURL, "");
    }
    catch (e) {
      // Opera solution
      if (typeof(opera)=="object") {
        a.rel="sidebar";
        a.title=pageTitle;
        a.url=pageURL;
        return true;
      } else {
        // The rest browsers (i.e Chrome, Safari)
        alert((navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Cmd' : 'Ctrl') + '+D 를 눌러 북마크에 추가해주세요.');
      }
    }
  }
  return false;
}
$(function() {
  $("#message_remove").click(function() {
    $(this).parent().parent().hide();
  });
});
