# React + three.js로 웹에서 3D 이미지 사용하기

## 무료 3D 이미지 다운로드

```bash
https://sketchfab.com/3d-models/duck-walk-free-415584bc3224484fba20a482592e2157
```

## GLTF 파일을 JSX Component로 바꾸기

```bash
npx gltfjsx scene.gltf
```

## Three.js Install

```bash
yarn add three
yarn add @react-three/fiber
yarn add @react-three/drei
```

## React Project 생성해 asset 넣기

![스크린샷](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/60b74e7f-e7c3-4ef2-b257-b9816e686f77/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-07-21_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.20.49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220720T163205Z&X-Amz-Expires=86400&X-Amz-Signature=c291bd11e5b48cf9cc5cc14124cdeb41158f79ff559285d9cae8f70aa4a88b17&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA%25202022-07-21%2520%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB%25201.20.49.png%22&x-id=GetObject)

## Example.jsx 생성

> Scene.js → jsx로 확장자 변경하여 import

```jsx
import { Suspense } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import styled from "styled-components";
import Model from "./Model";

const Example = () => {
  return (
    <>
      <Contain>
        <Canvas>
          <Suspense fallback={null}>
            <directionalLight intensity={1} />
            <ambientLight intensity={1.2} />
            <spotLight
              intensity={0.1}
              angle={0.1}
              penumbra={1}
              position={[10, 15, 10]}
              castShadow
            />
            <Model />
            <OrbitControls
              enablePan={true}
              enableZoom={true}
              enableRotate={true}
            />
          </Suspense>
        </Canvas>
      </Contain>
    </>
  );
};

const Contain = styled.div`
  margin: 0 auto;
  background: #2d2d2d;
`;

export default Example;
```

## 결과 확인

```
https://willowy-croquembouche-a988c9.netlify.app/
```
