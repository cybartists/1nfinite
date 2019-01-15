console.clear();

const canvas = document.querySelector('canvas');

const btn =new Button();
btn.label ="电压表";
canvas

const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    antialias: true
});
renderer.setClearColor(0xffdfdf);

const scene = new THREE.Scene();

const mouse = new THREE.Vector2();

const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientWidth, 1, 1000);
camera.position.z = 60;

const colors = [0xfb929e, 0xfff6f6, 0xaedefc]

class SmoothLine {
    constructor() {
        this.offset = 0;
        this.width = 0.2 + (Math.random() * 0.2);
        const colorIndex = Math.floor(Math.random() * colors.length);
        this.color = new THREE.Color(colors[colorIndex]);
        this.scale = Math.random() * 0.4 + 0.8;
        this.speed = Math.random() * 0.002 + 0.001;
        this.diameter = Math.random() * 14 + 6;
        this.opacity = Math.random() * 0.4 + 0.6;

        this.createLine();
    }

    createLine() {
        // Build an array of points
        const nbrOfPoints = 140;
        var geometry = new THREE.Geometry();
        const offsetZ = Math.random() * Math.PI;
        for (let i = 0; i < nbrOfPoints; i++) {
            const ratio = (i / nbrOfPoints) * Math.PI * 2 + (Math.PI / 2);
            var d = this.diameter;
            var x = d * (Math.cos(ratio + (Math.cos(ratio / 2))) * (1 - Math.sin(ratio))) / (1 + Math.pow(Math.sin(ratio), 2));
            var y = d * (Math.cos(ratio + (Math.cos(ratio / 2))) * (1 + Math.sin(ratio))) / (1 + Math.pow(Math.sin(ratio), 2));
            var z = Math.sin(ratio + offsetZ) * 20;
            geometry.vertices.push(new THREE.Vector3(x, y, z));
        }
        geometry.vertices.push(geometry.vertices[0]);

        this.line = new MeshLine();
        this.line.setGeometry(new THREE.Geometry().setFromPoints(new THREE.CatmullRomCurve3(geometry.vertices).getPoints(140)), function (p) {
            return 1 * Maf.parabola(p, 1)
        });
        // Build the material with good parameters to animate it.
        const material = new MeshLineMaterial({
            lineWidth: this.width,
            color: this.color,
            transparent: true,
            opacity: this.opacity,
            depthTest: false,
            dashArray: (Math.random() * 0.2 + 0.6),
            dashRatio: 0.7,
            dashOffset: Math.random()
        });

        // Build the Mesh
        this.mesh = new THREE.Mesh(this.line.geometry, material);
        this.mesh.position.x = (Math.random() - 0.5) * 3;
        this.mesh.position.y = (Math.random() - 0.5) * 3;
        this.mesh.position.z = (Math.random() - 0.5) * 5;
        this.mesh.rotation.z = Math.random() * Math.PI * 0.2 + 2;
        scene.add(this.mesh);
    }

    update() {
        this.mesh.material.uniforms.dashOffset.value += this.speed;
    }
}


const lines = [];
for (let i = 0; i < 100; i++) {
    lines.push(new SmoothLine());
}

const center = new THREE.Vector3();

function render() {
    requestAnimationFrame(render);

    lines.forEach((line) => {
        line.update();
    });

    camera.position.x = mouse.x * 3;
    camera.position.y = mouse.y * 3;
    camera.lookAt(center);

    renderer.render(scene, camera);
}

function onMouseMove(e) {
    const x = (e.clientX / (window.innerWidth * 0.5)) - 1;
    const y = -1 * (e.clientY / (window.innerHeight * 0.5)) + 1;
    updateMouse(x, y);
}

function onTouchMove(e) {
    const x = (e.touches[0].clientX / (window.innerWidth * 0.5)) - 1;
    const y = -1 * (e.touches[0].clientY / (window.innerHeight * 0.5)) + 1;
    updateMouse(x, y);
}

function updateMouse(x, y) {
    TweenMax.to(mouse, 1, {
        x,
        y,
        ease: Power1.easeOut
    })
}

window.addEventListener('mousemove', onMouseMove);
window.addEventListener('touchmove', onTouchMove);

function onResize() {
    renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
}

window.addEventListener('resize', onResize);
onResize();
requestAnimationFrame(render);