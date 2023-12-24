self.addEventListener('install', function(event){

	console.log('installed');
	event.waitUntil(
	    caches.open('static')
        .then(function (cache) {
            cache.addAll([
                '/static/images/fevicon3.png',
                '/static/vendors/bootstrap/dist/css/bootstrap.min.css',
                '/static/vendors/font-awesome/css/font-awesome.min.css',
                '/static/vendors/nprogress/nprogress.css',
                '/static/vendors/iCheck/skins/flat/green.css',
                '/static/vendors/bootstrap-progressbar/css/bootstrap-progressbar-3.3.4.min.css',
                '/static/vendors/jqvmap/dist/jqvmap.min.css',
                '/static/vendors/bootstrap-daterangepicker/daterangepicker.css',
                '/static/build/css/custom.min.css',
                '/static/css/buttons.dataTables.min.css',
                '/static/vendors/bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css',
                '/static/vendors/datatables.net-bs/css/dataTables.bootstrap.min.css',
                '/static/vendors/datatables.net-buttons-bs/css/buttons.bootstrap.min.css',
                '/static/vendors/datatables.net-fixedheader-bs/css/fixedHeader.bootstrap.min.css',
                '/static/vendors/datatables.net-responsive-bs/css/responsive.bootstrap.min.css',
                '/static/vendors/datatables.net-scroller-bs/css/scroller.bootstrap.min.css',
                '/static/vendors/fullcalendar/dist/fullcalendar.min.css',
                '/static/vendors/fullcalendar/dist/fullcalendar.print.css',
                '/static/vendors/jquery/dist/jquery.min.js',
                '/static/vendors/bootstrap/dist/js/bootstrap.min.js',
                '/static/vendors/nprogress/nprogress.js',
                '/static/vendors/gauge.js/dist/gauge.min.js',
                '/static/vendors/bootstrap-progressbar/bootstrap-progressbar.min.js',
                '/static/vendors/iCheck/icheck.min.js',
                '/static/vendors/skycons/skycons.js',
                '/static/vendors/Flot/jquery.flot.js',
                '/static/vendors/Flot/jquery.flot.pie.js',
                '/static/vendors/Flot/jquery.flot.time.js',
                '/static/vendors/Flot/jquery.flot.stack.js',
                '/static/vendors/Flot/jquery.flot.resize.js',
                '/static/vendors/flot.orderbars/js/jquery.flot.orderBars.js',
                '/static/vendors/flot-spline/js/jquery.flot.spline.min.js',
                '/static/vendors/flot.curvedlines/curvedLines.js',
                '/static/vendors/DateJS/build/date.js',
                '/static/vendors/jqvmap/dist/jquery.vmap.js',
                '/static/vendors/jqvmap/dist/maps/jquery.vmap.world.js',
                '/static/vendors/jqvmap/examples/js/jquery.vmap.sampledata.js',
                '/static/vendors/moment/min/moment.min.js',
                '/static/vendors/bootstrap-daterangepicker/daterangepicker.js',
                '/static/build/js/custom.min.js',
                '/static/vendors/fastclick/lib/fastclick.js',
                '/static/vendors/bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js',
                '/static/vendors/fullcalendar/dist/fullcalendar.min.js',
                '/static/vendors/datatables.net/js/jquery.dataTables.min.js',
                '/static/vendors/datatables.net-bs/js/dataTables.bootstrap.min.js',
                '/static/vendors/datatables.net-buttons/js/dataTables.buttons.min.js',
                '/static/vendors/datatables.net-buttons-bs/js/buttons.bootstrap.min.js',
                '/static/vendors/datatables.net-buttons/js/buttons.flash.min.js',
                '/static/vendors/datatables.net-buttons/js/buttons.html5.min.js',
                '/static/vendors/datatables.net-buttons/js/buttons.print.min.js',
                '/static/vendors/datatables.net-fixedheader/js/dataTables.fixedHeader.min.js',
                '/static/vendors/datatables.net-keytable/js/dataTables.keyTable.min.js',
                '/static/vendors/datatables.net-responsive/js/dataTables.responsive.min.js',
                '/static/vendors/datatables.net-responsive-bs/js/responsive.bootstrap.js',
                '/static/vendors/datatables.net-scroller/js/dataTables.scroller.min.js',
                '/static/vendors/jszip/dist/jszip.min.js',
                '/static/vendors/pdfmake/build/pdfmake.min.js',
                '/static/vendors/pdfmake/build/vfs_fonts.js',

            ]);

        })
    );

});

self.addEventListener('activate', function(event){
    console.log('activated');
});

self.addEventListener('fetch', function(event){
  event.respondWith(
      caches.match(event.request).then(function (res) {
          if (res){
              return res;
          }
          else {
              return fetch(event.request);
          }
      })
  )
  // return something for each interception
});/**
 * Created by anish on 15/7/19.
 */
