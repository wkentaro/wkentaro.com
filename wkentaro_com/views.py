import collections
import json
import os.path as osp
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

import flask
import jinja2


app = flask.Flask(__name__)


@app.route('/')
def index():
    repos = collections.OrderedDict([
        ('Computer Vision', [
            'wkentaro/labelme',
            'wkentaro/imgviz',
            'wkentaro/label-fusion',
            'wkentaro/pascal3d',
            'mikedh/trimesh',
            'aleju/imgaug',
        ]),
        ('Deep Learning', [
            'wkentaro/pytorch-fcn',
            'wkentaro/fcn',
            'wkentaro/chainer-mask-rcnn',
            'wkentaro/pytorch-for-numpy-users',
            'wkentaro/chainer-bicyclegan',
            'wkentaro/chainer-cyclegan',
            'wkentaro/real-harem',
            'chainer/chainer',
            'cupy/cupy',
        ]),
        ('Robotics', [
            # 'wkentaro/label_octomap',
            # 'wkentaro/hrp2_apc',
            'start-jsk/jsk_apc',
            'jsk-ros-pkg/jsk_recognition',
            'jsk-ros-pkg/jsk_visualization',
            # 'jsk-ros-pkg/jsk_common',
            'ros-perception/vision_opencv',
            'ros-perception/image_pipeline',
            'ros-perception/perception_pcl',
            # 'PointCloudLibrary/pcl',
            'ros/ros_comm',
            'ros/nodelet_core',
        ]),
        ('Utility', [
            'wkentaro/gdown',
            'wkentaro/gshell',
            'wkentaro/dotfiles',
            'wkentaro/pycd',
            'wkentaro/wstool_cd',
            # 'wkentaro/wkentaro.zsh-theme',
            'wkentaro/screenshot-manager',
            'wkentaro/gotenshita',
        ]),
    ])

    colors_url = 'https://raw.githubusercontent.com/ozh/github-colors/master/colors.json'  # NOQA
    try:
        response = urlopen(colors_url)
        colors = json.loads(response.read().decode('utf-8'))
    except Exception:
        colors = collections.defaultdict(lambda: {'color': '#000', 'url': ''})

    return flask.render_template(
        'index.html',
        repositories=repos,
        colors=colors,
    )


@app.route('/projects/<project_name>')
def projects(project_name):
    try:
        return flask.render_template(
            osp.join('projects', project_name + '.html'),
        )
    except jinja2.exceptions.TemplateNotFound:
        return flask.redirect('/')


# -----------------------------------------------------------------------------
# Redirects
# -----------------------------------------------------------------------------


@app.route('/projects/gsoc-2016')
def projects_gsoc_2016():
    return flask.redirect('/projects/gsoc2016')
