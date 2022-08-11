# React Router

## Nested Routes

> 중첩 라우팅

```javascript
function App() {
  return (
    <Routes>
      <Route path="posts" element={<Posts />}>
        <Route path=":postId" element={<Post />} />
        <Route path="notice" element={<Notice />} />
      </Route>
    </Routes>
  );
}
```

- 주의사항1: nested된 child route는 상위 route element들의 child component로 그려진다
- 주의사항2: 부모 route의 element에는 <Outlet>을 넣어야 하며 여기에 자식 element가 그려진다.
