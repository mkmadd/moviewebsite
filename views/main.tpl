<!DOCTYPE html>
<html lang="en">
% include('header.tpl', css_file='/static/main.css', 
%           js_file='/static/main.js')
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Michael's Favorite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      % for i, movie in enumerate(movies):
        % include('movie_tile.tpl', movie=movie, index=str(i))
      % end
    </div>
  </body>
</html>