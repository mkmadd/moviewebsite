    <head>
        <meta charset="utf-8">
        <title>{{title if defined('title') else "Michael's Favorite Movies"}}</title>
    
        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

        <!-- If additional css and js files have been passed in, add them -->
        % if defined('css_file'):
        <link rel="stylesheet" type="text/css" href="{{css_file}}">
        % end

        % if defined('js_file'):
        <script src="{{js_file}}"></script>
        % end
    </head>
