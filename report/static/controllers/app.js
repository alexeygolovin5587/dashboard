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

        $rootScope.pass_data = {
            user: '',
            profile: ''
        }

        $rootScope.IP = "54.187.32.139"
        $rootScope.PORT = '80'

				$rootScope.formData = null
        $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
            var requireLogin = toState.data.requireLogin;

            if (requireLogin && $rootScope.is_authenticated == false) {
                $location.path('/login');
              // get me a login modal!
            }
          });
    })
    .directive('myDirective', function ($rootScope, httpPostFactory) {
        return {
            restrict: 'A',
            scope: true,
            link: function (scope, element, attr) {
                element.bind('change', function () {
                    var formData = new FormData();
                    formData.append('file', element[0].files[0]);
										$rootScope.formData = formData
                    
                });

            }
        };
    })

    .factory('httpPostFactory', function ($http) {
        return function (file, data, callback) {
            $http({
                url: file,
                method: "POST",
                data: data,
                headers: {'Content-Type': undefined}
            }).success(function (response) {
                callback(response);
            });
        };
    })
})();

