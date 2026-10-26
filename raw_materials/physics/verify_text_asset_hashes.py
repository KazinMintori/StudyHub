"""Check portable text fingerprints while preserving strict original image/PDF bytes."""
from pathlib import Path
import ast,hashlib,json,tempfile
ROOT=Path(__file__).resolve().parents[2]
checks=[]
for chapter in [1,3]:
 source=ROOT/f'raw_materials/physics/verify_chapter{chapter}_partial_exercises.py'
 tree=ast.parse(source.read_text(encoding='utf-8'))
 function=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='sha256_asset')
 namespace={'hashlib':hashlib}
 # Extract only the first-party hashing function, not the numerical verifier's body.
 exec(compile(ast.Module(body=[function],type_ignores=[]),str(source),'exec'),namespace)
 fingerprint=namespace['sha256_asset']
 with tempfile.TemporaryDirectory(prefix='studyhub-text-hash-')as directory:
  folder=Path(directory)
  for extension,content in [('md',b'$$\nn=mg\n$$\n'),('svg',b'<svg>\n<text>n=mg</text>\n</svg>\n')]:
   a=folder/f'lf.{extension}';b=folder/f'crlf.{extension}';changed=folder/f'changed.{extension}'
   a.write_bytes(content);b.write_bytes(content.replace(b'\n',b'\r\n'))
   changed.write_bytes(content.replace(b'n=mg',b'n=-mg'))
   assert fingerprint(a)==fingerprint(b)==hashlib.sha256(content).hexdigest()
   assert fingerprint(changed)!=fingerprint(a)
   checks.append({'chapter':chapter,'type':extension,'LFAndCRLFAgree':True,'MeaningfulContentMutationDetected':True})
  for extension,content in [('png',b'\x89PNG\r\n\x1a\nRAW\r\nDATA'),('pdf',b'%PDF-1.7\r\nRAW\r\nDATA')]:
   original=folder/f'original.{extension}';changed=folder/f'changed.{extension}'
   original.write_bytes(content);changed.write_bytes(content.replace(b'\r\n',b'\n'))
   assert fingerprint(original)==hashlib.sha256(content).hexdigest()
   assert fingerprint(original)!=fingerprint(changed)
   checks.append({'chapter':chapter,'type':extension,'OriginalBytesHashedStrictly':True,'BinaryByteMutationDetected':True})
print(json.dumps({'status':'passed','cases':len(checks),'checks':checks},ensure_ascii=False))
