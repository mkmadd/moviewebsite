<!DOCTYPE html>
<html lang="en">
% include('header.tpl', title=movie.title, css_file='/static/movie.css')
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="/"><span class="glyphicon glyphicon-home"></span></a>
            <p class="navbar-text"><b>{{movie.title}} - one of my favorites</b></p>
          </div>
        </div>
      </div>
    </div>
    <main class="container">
        <div class="row">
            <div class="col-sm-4">
                <img src="{{movie.poster_image_url}}" width="220" height="342">
            </div>
            <div class="col-sm-8">
                <div class="row">
                    <div class="col-sm-12">
                        <h2>{{movie.title}} ({{movie.year}})</h2>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <h3>MPAA Rating</h3>
                        <p>{{movie.mpaa_rating}}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <h3>Synopsis</h3>
                        <p>{{movie.synopsis if movie.synopsis else 'No Synopsis Provided.'}}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <h3>Ratings (from Rotten Tomatoes)</h3>
                        <ul>
                            <li>Critics' Score - {{movie.critics_ratings['critics']}}</li>
                            <li>Audience's Score - {{movie.critics_ratings['audience']}}</li>
                        </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <h3>Director{{'s' if len(movie.directors) > 1 else ''}}</h3>
                        <ul>
                        % for director in movie.directors:
                            <li>{{director}}</li>
                        % end
                        </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <h3>Cast</h3>
                        <ul>
                        % for actor in movie.cast:
                            <li>{{actor}}</li>
                        % end
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <footer>
        <div class="text-center">
            <p>Information on this page provided by Rotten Tomatoes; 
            check out their page for 
            <a href="{{movie.rotten_url}}">{{movie.title}}</a>!</p>
        </div>
    </footer>
  </body>
</html>