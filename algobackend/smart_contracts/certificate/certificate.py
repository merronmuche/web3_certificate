import beaker as bk
import pyteal as pt

class CertificateState:
    certificate_count = bk.GlobalStateValue(pt.TealType.uint64)

app = bk.Application("CertificateApp", state=CertificateState())

@pt.Subroutine
def create_certificate():
    certificate_count = app.certificate_count.get()
    new_certificate_count = certificate_count + pt.Int(1)
    app.certificate_count.set(new_certificate_count)
    return new_certificate_count

if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")
