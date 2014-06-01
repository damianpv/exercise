
// Facebook Friend
angular.module('FriendFB', [])
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//');
        $interpolateProvider.endSymbol('//');
    })
    .controller('Controller', function($scope, $http){
        // TODO: needs to be a domain for Facebook app. ex: sitio.com
        $http.get('http://matrix.com:8000/api/friends/').success(function(data){
            $scope.friends = data;
        });
    });
