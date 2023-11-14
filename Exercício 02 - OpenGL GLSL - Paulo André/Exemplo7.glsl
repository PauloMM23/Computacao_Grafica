#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359

uniform vec2 u_resolution;
uniform float u_time;

mat2 rotate2d(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}

float box(in vec2 _st, in vec2 _size){
    _size = vec2(0.5) - _size*0.5;
    vec2 uv = smoothstep(_size,
                        _size+vec2(0.001),
                        _st);
    uv *= smoothstep(_size,
                    _size+vec2(0.001),
                    vec2(1.0)-_st);
    return uv.x*uv.y;
}

float square(in vec2 _st, float _size){
    return  box(_st, vec2(_size,_size/1.));
}

void main(){
    vec2 st = gl_FragCoord.xy/u_resolution.xy;
    vec3 color = vec3(0.0, 0.051, 0.7451);

    st -= vec2(0.5);
    
    st = rotate2d( sin(u_time)*PI ) * st;
    
    st += vec2(0.3);

    color += vec3(square(st,0.2));

    gl_FragColor = vec4(color,1.0);
}
