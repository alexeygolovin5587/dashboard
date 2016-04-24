/**
 * INSPINIA - Responsive Admin Theme
 *
 * Inspinia theme use AngularUI Router to manage routing and views
 * Each view are defined as state.
 * Initial there are written state for all view in theme.
 *
 */
function config($stateProvider, $urlRouterProvider, $ocLazyLoadProvider) {
    $urlRouterProvider.otherwise("/login");

    $ocLazyLoadProvider.config({
        // Set to true if you want to see what and when is dynamically loaded
        debug: false
    });

    $stateProvider
        .state('index', {
            abstract: true,
            url: "/index",
            templateUrl: "views/common/content.html",
            data: {
                requireLogin: true // this property will apply to all children of 'app'
              }
        })
        .state('index.main', {
            url: "/main",
            templateUrl: "views/Charts.html",
            data: { pageTitle: 'Example view' },
            resolve: {
                loadPlugin: function ($ocLazyLoad, $rootScope) {

                    return $ocLazyLoad.load([
                        {
                            files: $rootScope.source
                        }
                    ]);
                }
            }
        })
        .state('login', {
            url: "/login",
            templateUrl: "views/Login.html",
            data: { pageTitle: 'Example view' }
        })
}
angular
    .module('dashboard')
    .config(config)
    .run(function($rootScope, $state) {
        $rootScope.$state = $state;
        $rootScope.source = ['script/jquery-1.10.2.min.js', 'script/jquery-migrate-1.2.1.min.js', 'script/jquery-ui.js', 'script/bootstrap.min.js', 'script/bootstrap-hover-dropdown.js', 'script/html5shiv.js', 'script/respond.min.js', 'script/jquery.metisMenu.js', 'script/jquery.slimscroll.js', 'script/jquery.cookie.js', 'script/icheck.min.js', 'script/jquery.news-ticker.js', 'script/jquery.menu.js', 'script/pace.min.js', 'script/holder.js', 'script/responsive-tabs.js', 'script/jquery.flot.js', 'script/jquery.flot.categories.js', 'script/jquery.flot.pie.js', 'script/jquery.flot.tooltip.js', 'script/jquery.flot.resize.js', 'script/jquery.flot.fillbetween.js', 'script/jquery.flot.stack.js', 'script/jquery.flot.spline.js', 'script/zabuto_calendar.min.js']
    });
