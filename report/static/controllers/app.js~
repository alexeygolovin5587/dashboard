/**
 * DASHBOARD - Responsive Admin Theme
 *
 */
(function () {
    angular.module('dashboard', [
        'ui.router',                    // Routing
        'oc.lazyLoad',                  // ocLazyLoad
    ])
    .run(function ($rootScope, $http, $state, $location) {
        $rootScope.user = {
            username: '',
            password: '',
        };
        $rootScope.is_authenticated = false;

        $rootScope.IP = "54.187.32.139"
        $rootScope.PORT = '80'
        $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
            var requireLogin = toState.data.requireLogin;

            if (requireLogin && $rootScope.is_authenticated == false) {
                $location.path('/login');
              // get me a login modal!
            }
          });
    })
})();

