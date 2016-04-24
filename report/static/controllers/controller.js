/**
 * INSPINIA - Responsive Admin Theme
 *
 */

/**
 * MainCtrl - controller
 */
function MainCtrl($scope) {
    //BEGIN LINE CHART
    $scope.d1_1 = [["Jan", 200],["Feb", 201],["Mar", 199],["Apr", 187],["May", 193],["Jun", 192],["Jul", 206],["Aug", 186],["Sep", 206]];
    $scope.d1_2 = [["Jan", 122],["Feb", 170],["Mar", 163],["Apr", 161],["May", 122],["Jun", 136],["Jul", 130],["Aug", 128],["Sep", 148]];
    $scope.d1_3 = [["Jan", 81],["Feb", 92],["Mar", 98],["Apr", 102],["May", 80],["Jun", 97],["Jul", 86],["Aug", 105],["Sep", 85]];


};

function Login($scope, $http, $filter, $rootScope, $location) {
    $scope.user = {
        username: '',
        password: '',
    };

    $scope.show = false;

    $scope.login = function () {
		url = 'http://localhost:8000/login/';
        if($scope.user.username == undefined || $scope.user.password ==undefined)
            return;
        var parameter = JSON.stringify($scope.user);

        $http.post(url, parameter)
            .success(function(response) {
                if(response.login == 'success') {
                    $rootScope.user.username = $scope.user.username;
                    $rootScope.user.password = $scope.user.password;
                    $rootScope.is_authenticated = true;

                    $location.path('/index/main')

                    $scope.show = false;
                }
                else{
                    $scope.show = true;
                }
            });
	}

    $scope.logout = function () {

        $rootScope.user.username = undefined;
        $rootScope.user.password = undefined;
        $rootScope.is_authenticated = false;

        $location.path('/login')

	}
}

angular
    .module('dashboard')
    .controller('MainCtrl', MainCtrl)
    .controller('Login', Login)